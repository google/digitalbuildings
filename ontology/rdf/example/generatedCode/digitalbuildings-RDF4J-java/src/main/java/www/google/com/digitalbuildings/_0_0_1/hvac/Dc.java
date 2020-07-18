package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.Equipment;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_percentage_command;

/**
* Class Dc 
* Tag for dry coolers (sensible, closed-loop coolers).
*/
@SuppressWarnings("serial")
public class Dc extends www.google.com.digitalbuildings._0_0_1.Equipment implements IDc{

	IRI newInstance;
	public Dc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsCooling_percentage_command (ICooling_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ICooling_percentage_command> getUsesOptionalsCooling_percentage_command (){
		Set<ICooling_percentage_command> UsesOptionalsCooling_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_percentage_command) {
				UsesOptionalsCooling_percentage_command.add((Cooling_percentage_command)action);
			}
		});
		return UsesOptionalsCooling_percentage_command;
	}

	public static Set<IDc> getAllDcsObjectsCreated(){
		Set<IDc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dc")).subjects().stream()
		.map(mapper->(IDc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}