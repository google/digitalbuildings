package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IZone;
import www.google.com.digitalbuildings._0_0_1.subfields.Zone;
import www.google.com.digitalbuildings._0_0_1.subfields.ICo2;
import www.google.com.digitalbuildings._0_0_1.subfields.Co2;
import www.google.com.digitalbuildings._0_0_1.subfields.ISetpoint;
import www.google.com.digitalbuildings._0_0_1.subfields.Setpoint;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.Air;
import www.google.com.digitalbuildings._0_0_1.subfields.IConcentration;
import www.google.com.digitalbuildings._0_0_1.subfields.Concentration;


@SuppressWarnings("serial")
public class Zone_air_co2_concentration_setpoint extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IZone_air_co2_concentration_setpoint{

	IRI newInstance;
	public Zone_air_co2_concentration_setpoint(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Zone_air_co2_concentration_setpoint"));
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


  public void addComposedOfCo2 (ICo2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ICo2> getComposedOfCo2 (){
		Set<ICo2> ComposedOfCo2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Co2) {
				ComposedOfCo2.add((Co2)action);
			}
		});
		return ComposedOfCo2;
	}


  public void addComposedOfConcentration (IConcentration parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IConcentration> getComposedOfConcentration (){
		Set<IConcentration> ComposedOfConcentration = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Concentration) {
				ComposedOfConcentration.add((Concentration)action);
			}
		});
		return ComposedOfConcentration;
	}


  public void addComposedOfSetpoint (ISetpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ISetpoint> getComposedOfSetpoint (){
		Set<ISetpoint> ComposedOfSetpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Setpoint) {
				ComposedOfSetpoint.add((Setpoint)action);
			}
		});
		return ComposedOfSetpoint;
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

	public static Set<IZone_air_co2_concentration_setpoint> getAllZone_air_co2_concentration_setpointsObjectsCreated(){
		Set<IZone_air_co2_concentration_setpoint> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Zone_air_co2_concentration_setpoint")).subjects().stream()
		.map(mapper->(IZone_air_co2_concentration_setpoint)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}