package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IUse;
import www.google.com.digitalbuildings._0_0_1.subfields.Use;
import www.google.com.digitalbuildings._0_0_1.subfields.IZone;
import www.google.com.digitalbuildings._0_0_1.subfields.Zone;
import www.google.com.digitalbuildings._0_0_1.subfields.ILabel;
import www.google.com.digitalbuildings._0_0_1.subfields.Label;


@SuppressWarnings("serial")
public class Zone_use_label extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IZone_use_label{

	IRI newInstance;
	public Zone_use_label(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Zone_use_label"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfLabel (ILabel parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ILabel> getComposedOfLabel (){
		Set<ILabel> ComposedOfLabel = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Label) {
				ComposedOfLabel.add((Label)action);
			}
		});
		return ComposedOfLabel;
	}


  public void addComposedOfUse (IUse parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IUse> getComposedOfUse (){
		Set<IUse> ComposedOfUse = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Use) {
				ComposedOfUse.add((Use)action);
			}
		});
		return ComposedOfUse;
	}


  public void addComposedOfZone (IZone parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IZone> getComposedOfZone (){
		Set<IZone> ComposedOfZone = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Zone) {
				ComposedOfZone.add((Zone)action);
			}
		});
		return ComposedOfZone;
	}

	public static Set<IZone_use_label> getAllZone_use_labelsObjectsCreated(){
		Set<IZone_use_label> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Zone_use_label")).subjects().stream()
		.map(mapper->(IZone_use_label)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}