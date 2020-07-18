package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.ICooling;
import www.google.com.digitalbuildings._0_0_1.subfields.Cooling;
import www.google.com.digitalbuildings._0_0_1.subfields.ICommand;
import www.google.com.digitalbuildings._0_0_1.subfields.Command;
import www.google.com.digitalbuildings._0_0_1.subfields.IPercentage;
import www.google.com.digitalbuildings._0_0_1.subfields.Percentage;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.Air;
import www.google.com.digitalbuildings._0_0_1.subfields.IDamper;
import www.google.com.digitalbuildings._0_0_1.subfields.Damper;


@SuppressWarnings("serial")
public class Cooling_air_damper_percentage_command_1 extends www.google.com.digitalbuildings._0_0_1.fields.Field implements ICooling_air_damper_percentage_command_1{

	IRI newInstance;
	public Cooling_air_damper_percentage_command_1(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Cooling_air_damper_percentage_command_1"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfAir (IAir parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IAir> getComposedOfAir (){
		Set<IAir> ComposedOfAir = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Air) {
				ComposedOfAir.add((Air)action);
			}
		});
		return ComposedOfAir;
	}


  public void addComposedOfCommand (ICommand parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ICommand> getComposedOfCommand (){
		Set<ICommand> ComposedOfCommand = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Command) {
				ComposedOfCommand.add((Command)action);
			}
		});
		return ComposedOfCommand;
	}


  public void addComposedOfCooling (ICooling parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ICooling> getComposedOfCooling (){
		Set<ICooling> ComposedOfCooling = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling) {
				ComposedOfCooling.add((Cooling)action);
			}
		});
		return ComposedOfCooling;
	}


  public void addComposedOfDamper (IDamper parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IDamper> getComposedOfDamper (){
		Set<IDamper> ComposedOfDamper = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Damper) {
				ComposedOfDamper.add((Damper)action);
			}
		});
		return ComposedOfDamper;
	}


  public void addComposedOfPercentage (IPercentage parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IPercentage> getComposedOfPercentage (){
		Set<IPercentage> ComposedOfPercentage = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Percentage) {
				ComposedOfPercentage.add((Percentage)action);
			}
		});
		return ComposedOfPercentage;
	}

	public static Set<ICooling_air_damper_percentage_command_1> getAllCooling_air_damper_percentage_command_1sObjectsCreated(){
		Set<ICooling_air_damper_percentage_command_1> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Cooling_air_damper_percentage_command_1")).subjects().stream()
		.map(mapper->(ICooling_air_damper_percentage_command_1)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}