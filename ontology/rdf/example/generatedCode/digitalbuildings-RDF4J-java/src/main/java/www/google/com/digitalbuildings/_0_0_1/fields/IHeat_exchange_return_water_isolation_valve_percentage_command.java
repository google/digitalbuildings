package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IExchange;
import www.google.com.digitalbuildings._0_0_1.subfields.IWater;
import www.google.com.digitalbuildings._0_0_1.subfields.IHeat;
import www.google.com.digitalbuildings._0_0_1.subfields.IReturn;
import www.google.com.digitalbuildings._0_0_1.subfields.ICommand;
import www.google.com.digitalbuildings._0_0_1.subfields.IPercentage;
import www.google.com.digitalbuildings._0_0_1.subfields.IIsolation;
import www.google.com.digitalbuildings._0_0_1.subfields.IValve;

public interface IHeat_exchange_return_water_isolation_valve_percentage_command extends IField{

	public IRI iri();

    public void addComposedOfCommand (ICommand parameter);

	public Set<ICommand> getComposedOfCommand();

    public void addComposedOfExchange (IExchange parameter);

	public Set<IExchange> getComposedOfExchange();

    public void addComposedOfHeat (IHeat parameter);

	public Set<IHeat> getComposedOfHeat();

    public void addComposedOfIsolation (IIsolation parameter);

	public Set<IIsolation> getComposedOfIsolation();

    public void addComposedOfPercentage (IPercentage parameter);

	public Set<IPercentage> getComposedOfPercentage();

    public void addComposedOfReturn (IReturn parameter);

	public Set<IReturn> getComposedOfReturn();

    public void addComposedOfValve (IValve parameter);

	public Set<IValve> getComposedOfValve();

    public void addComposedOfWater (IWater parameter);

	public Set<IWater> getComposedOfWater();

}