package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.Equipment;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_use_label;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_use_label;

/**
* Class Vav 
* Tag for terminal units with variable volume control.
*/
@SuppressWarnings("serial")
public class Vav extends www.google.com.digitalbuildings._0_0_1.Equipment implements IVav{

	IRI newInstance;
	public Vav(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Vav"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsZone_use_label (IZone_use_label parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IZone_use_label> getUsesOptionalsZone_use_label (){
		Set<IZone_use_label> UsesOptionalsZone_use_label = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_use_label) {
				UsesOptionalsZone_use_label.add((Zone_use_label)action);
			}
		});
		return UsesOptionalsZone_use_label;
	}

	public static Set<IVav> getAllVavsObjectsCreated(){
		Set<IVav> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Vav")).subjects().stream()
		.map(mapper->(IVav)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}